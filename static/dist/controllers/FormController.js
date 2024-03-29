import { FormRenderer } from "../renderer/FormRenderer.js";
import { FormRepository } from "../repository/FormRepository.js";
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
        FormController.manageSentService(formDTO);
    }
    static manageSentService(formDTO) {
        FormRepository.registerStudent(formDTO)
            .then(response => {
            if (response.success) {
                FormRenderer.showsStatusInfo(true, response.msg);
            }
            else {
                FormRenderer.showsStatusInfo(false, response.msg);
            }
        })
            .catch(error => {
            FormRenderer.showsStatusInfo(false, 'There was an error in the request');
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
            const newValue = htmlInput.value || '';
            newInputs.push({ ...input, value: newValue });
        });
        return newInputs;
    }
}
