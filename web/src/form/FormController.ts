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
import { Form, SubmitAction } from "./Form";
import { FormRepository } from "./FormRepository";

export class FormController {

   #repository: FormRepository

   constructor () {
      this.#repository = new FormRepository;
   }

   static submitForm () {
      
   }

   static validateForm (form: Form, formElem: HTMLFormElement) {
      return
   }
}