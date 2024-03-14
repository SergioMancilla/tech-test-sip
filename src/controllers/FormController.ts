import { Form, Input } from "../models/Form.js";
import { FormRenderer } from "../renderer/FormRenderer.js";
import { FormRepository } from "../repository/FormRepository.js";

type InputForValidate = Required<Pick<Input, 'name' | 'id' | 'value' | 'validators'>>

export class FormController {

   constructor () {
      
   }

   static submitForm (form: Form) {
      FormRenderer.removeAllErrorMsg()

      const formDTO: { [key: string]: string } = {}
      const newInputs = FormController.getNewInputs(form)
      if (!FormController.validate(newInputs)) return

      newInputs.forEach((input) => {
         formDTO[input.name] = input.value
      })

      FormController.manageSentService(formDTO)
   }

   static manageSentService (formDTO: { [key: string]: string }) {
      FormRepository.registerStudent(formDTO)
      .then(success => {
         if (success) {
            FormRenderer.showsStatusInfo(true, 'Student saved successfully')
         } else {
            FormRenderer.showsStatusInfo(false, 'The server refused the data')
         }
      })
      .catch(error => {
         FormRenderer.showsStatusInfo(false, 'There was an error in the request')
      })
   }

   static validate (newInputs: InputForValidate[]): boolean {
      const fields = newInputs.map(({ id, value, validators }) => {
         return validators.every((validator) => {
            const {val, msg} = validator(value)
            if (!val) FormRenderer.showErrorMsg(id, msg)
            return val
         })
      })
      
      return !fields.includes(false)
   }

   static getNewInputs (form: Form): InputForValidate[] {
      const newInputs = new Array<InputForValidate>
      form.getInputs().forEach(input => {
         const htmlInput = <HTMLInputElement>document.getElementById(input.id)
         const newValue = htmlInput.value || ''
         newInputs.push({...input, value: newValue})
      });
      return newInputs
   }
}