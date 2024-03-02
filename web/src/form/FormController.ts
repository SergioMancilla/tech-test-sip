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
import { FormRepository } from "./FormRepository.js";

type InputForValidate = Required<Pick<Input, 'value' | 'validators'>>

export class FormController {

   #repository: FormRepository

   constructor () {
      this.#repository = new FormRepository;
   }

   static submitForm (form: Form) {
      console.log('pepino')
      const newInputs = FormController.getNewInputs(form)
      FormController.validate(newInputs)
   }

   static validate (newInputs: InputForValidate[]): boolean {
      return newInputs.every(({ value, validators }) => {
          validators.every((validator) => validator(value))
      })
   }

   static getNewInputs (form: Form): InputForValidate[] {
      const newInputs = new Array<InputForValidate>
      form.getInputs().forEach(input => {
         const htmlInput = <HTMLInputElement>document.getElementById(input.id)
         newInputs.push({
            value: htmlInput? htmlInput.value : '',
            validators: input.validators
         })
      });
      console.log(newInputs)
      return newInputs
   }
}