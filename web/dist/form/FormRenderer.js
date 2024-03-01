export class FormRenderer {
    static renderForm(form, formContainerId) {
        const formContainer = document.getElementById(formContainerId);
        if (!formContainer)
            throw new Error('Invalid container');
        const formElem = FormRenderer.#createHtmlForm(form);
        formContainer.appendChild(formElem);
    }
    static #createHtmlForm(form) {
        const formElem = document.createElement('form');
        formElem.setAttribute('action', form.getAction());
        formElem.setAttribute('method', form.getMethod());
        const htmlInputs = FormRenderer.#createHtmlInputs(form.getInputs());
        const htmlButton = FormRenderer.#createSubmitButton(form.getSubitAction(), 'Create');
        const inputsContainer = document.createElement('div');
        inputsContainer.classList.add('inputs-container');
        htmlInputs.forEach(input => {
            inputsContainer.appendChild(input);
        });
        formElem.appendChild(inputsContainer);
        formElem.appendChild(htmlButton);
        return formElem;
    }
    static #createHtmlInputs(inputs) {
        return inputs.map((input) => {
            const inputElem = document.createElement('input');
            // Creating HTML inputs through attributes in Input objects
            inputElem.setAttribute('type', input.type);
            inputElem.setAttribute('name', input.name);
            inputElem.classList.add('form-control');
            if (input.placeholder)
                inputElem.setAttribute('placeholder', input.placeholder);
            if (input.title)
                inputElem.setAttribute('title', input.title);
            if (input.value)
                inputElem.setAttribute('value', input.value);
            const label = document.createElement('label');
            label.textContent = input.label;
            label.appendChild(inputElem);
            return label;
        });
    }
    static #createSubmitButton(onSubmit, buttonText = 'Send') {
        const btnElem = document.createElement('button');
        btnElem.setAttribute('type', 'submit');
        btnElem.classList.add('btn');
        btnElem.textContent = buttonText;
        btnElem.onclick = onSubmit;
        return btnElem;
    }
}
