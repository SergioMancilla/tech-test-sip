export class FormRenderer {
    static renderForm(form, formContainerId) {
        const formContainer = document.getElementById(formContainerId);
        if (!formContainer)
            throw new Error('Invalid container');
        const formElem = FormRenderer.#createHtmlForm(form);
        formContainer.appendChild(formElem);
        const submitButton = document.getElementById('submit-button');
        submitButton.addEventListener('click', (event) => {
            event.preventDefault();
            form.runSubmitAction(form);
        });
    }
    static #createHtmlForm(form) {
        const formElem = document.createElement('form');
        formElem.setAttribute('action', form.getAction());
        formElem.setAttribute('method', form.getMethod());
        const htmlInputs = FormRenderer.#createHtmlInputs(form.getInputs());
        const htmlButton = FormRenderer.#createSubmitButton('Create');
        const inputsContainer = document.createElement('div');
        inputsContainer.classList.add('inputs-container');
        htmlInputs.forEach(input => {
            inputsContainer.innerHTML += input;
        });
        if (form.getTitle)
            formElem.innerHTML += `<h2>${form.getTitle()}</h2>`;
        formElem.appendChild(inputsContainer);
        formElem.innerHTML += htmlButton;
        return formElem;
    }
    static #createHtmlInputs(inputs) {
        return inputs.map((input) => {
            return `
            <label>
                ${input.label}
                <input type=${input.type} name=${input.name} class="form-control" placeholder=${input.placeholder ?? ''} title=${input.title ?? ''} title=${input.value ?? ''}>
            </label>
            `;
        });
    }
    static #createSubmitButton(buttonText = 'Send') {
        return `
            <button id="submit-button" type="submit" class="btn btn-primary">
                ${buttonText}
            </button>
        `;
    }
}
