import { FormRenderer } from "../renderer/FormRenderer.js";
export class FormController {
    constructor() {
    }
    static submitForm(form) {
        FormRenderer.removeAllErrorMsg();
        const formDTO = {};
        const newInputs = FormController.getNewInputs(form);
        if (!FormController.validate(newInputs))
            return;
        newInputs.forEach((input) => {
            formDTO[input.name] = input.value;
        });
    }
    static validate(newInputs) {
        const fields = newInputs.map(({ id, value, validators }) => {
            return validators.every((validator) => {
                const { val, msg } = validator(value);
                if (!val)
                    FormRenderer.showErrorMsg(id, msg);
                return val;
            });
        });
        return !fields.includes(false);
    }
    static getNewInputs(form) {
        const newInputs = new Array;
        form.getInputs().forEach(input => {
            const htmlInput = document.getElementById(input.id);
            newInputs.push({ value: htmlInput ? htmlInput.value : '', ...input });
        });
        console.log(newInputs);
        return newInputs;
    }
}
