import { FormRepository } from "./FormRepository";
export class FormController {
    #repository;
    constructor() {
        this.#repository = new FormRepository;
    }
    static submitForm() {
    }
    static validateForm(form, formElem) {
        return;
    }
}
