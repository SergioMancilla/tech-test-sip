import { validators } from '../utils/validators.js'
import { Form, Input, SubmitAction } from './Form.js'

export class FormRenderer {
    static renderForm(form: Form, formContainerId: string) {
        const formContainer = document.getElementById(formContainerId)
        if (!formContainer) throw new Error('Invalid container')

        const formElem = FormRenderer.#createHtmlForm(form)
        formContainer.appendChild(formElem)

        const submitButton = document.getElementById('submit-button');
        submitButton!.addEventListener('click', (event) => {
            event.preventDefault()
            form.runSubmitAction()
        });

        form.getInputs().forEach((input) => {
            document.getElementById(input.id)?.addEventListener('change', () => {
                FormRenderer.removeErrorMsg(input.id)
            })
        })
    }

    static #createHtmlForm (form: Form): HTMLFormElement {
        const formElem = document.createElement('form')
        formElem.setAttribute('action', form.getAction())
        formElem.setAttribute('method', form.getMethod())

        const htmlInputs = FormRenderer.#createHtmlInputs(form.getInputs())
        const htmlButton = FormRenderer.#createSubmitButton('Create')
        const inputsContainer = document.createElement('div')
        inputsContainer.classList.add('inputs-container')

        htmlInputs.forEach(input => {
            inputsContainer.innerHTML += input
        })

        if (form.getTitle) formElem.innerHTML += `<h2>${form.getTitle()}</h2>`
        formElem.appendChild(inputsContainer)
        formElem.innerHTML += htmlButton
        formElem.innerHTML += '<span class="text-sm">Fields with * are required</span>'
        return formElem
    }

    static #createHtmlInputs (inputs: Input[]): string[] {
        return inputs.map((input) => {
            return `
            <label title=${input.title?? ''} >
                ${input.label} ${input.validators.includes(validators.required)? '*' : ''}
                <input id=${input.id} type=${input.type} name=${input.name} class="form-control" placeholder=${input.placeholder?? ''} title='${input.title?? ''}' value=${input.value?? ''} >
                <p class="error-msg text-danger text-center"></p>
            </label>
            `
        })
    }

    static #createSubmitButton (buttonText: string = 'Send'): string {
        return `
            <button id="submit-button" type="submit" class="btn btn-primary">
                ${buttonText}
            </button>
        `;
    }

    static showErrorMsg (elemId: string, msg: string) {
        const input = document.getElementById(elemId)
        const errorElement = input?.nextElementSibling

        if (errorElement && errorElement.classList.contains('error-msg')) {
            errorElement.textContent = msg
        }
    }

    static removeErrorMsg (elemId: string) {
        const input = document.getElementById(elemId)
        const errorElement = input?.nextElementSibling

        if (errorElement && errorElement.classList.contains('error-msg')) {
            errorElement.textContent = ''
        }
    }

    static removeAllErrorMsg () {
        document.querySelectorAll('.error-msg').forEach((element) => {
            element.textContent = ''
        })
    }
}