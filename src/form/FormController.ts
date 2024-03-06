/*
FLUJO DE UN FORMULARIO:
1. Model define la estructura del formulario
2. Se crea el formulario en el Factory usando el Model
3. Renderer lo renderiza
4. Controller se encarga de enviar el formulario, validar los datos, etc, le delega
   la responsabilidad de enviar al backend a Repository
5. Repository maneja el envío al backend y las respuestas, que las retorna para que
   controller pueda hacer lo suyo
*/
import { Form, Input } from "./Form.js";
import { FormRenderer } from "./FormRenderer.js";
import { FormRepository } from "./FormRepository.js";

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

      FormRepository.registerStudent(formDTO)
      // .then((res) => {return res.json()})
      // .then((res) => {
      //    console.log(res)
      // })
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
         newInputs.push({value: htmlInput? htmlInput.value : '', ...input})
      });
      return newInputs
   }
}