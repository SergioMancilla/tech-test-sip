import { FormRepository } from "./FormRepository.js";
export class FormController {
    #repository;
    constructor() {
        this.#repository = new FormRepository;
    }
    static submitForm(form) {
        console.log('pepino');
        const newInputs = FormController.getNewInputs(form);
        FormController.validate(newInputs);
    }
    static validate(newInputs) {
        return newInputs.every(({ value, validators }) => {
            validators.every((validator) => validator(value));
        });
    }
    static getNewInputs(form) {
        const newInputs = new Array;
        form.getInputs().forEach(input => {
            const htmlInput = document.getElementById(input.id);
            newInputs.push({
                value: htmlInput ? htmlInput.value : '',
                validators: input.validators
            });
        });
        console.log(newInputs);
        return newInputs;
    }
}
