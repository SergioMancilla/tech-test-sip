type Validator = (value: string) => boolean

interface Input {
    type: string
    name: string
    label: string
    placeholder?: string
    title?: string
    value?: string
    validators: Validator[]
}

interface Button {
    type: 'submit' | 'text'
    text: string
    callback: () => {}
}

class Form {
    #inputs: Input[]

    #inputsHTML: HTMLLabelElement[]
    #button: HTMLButtonElement
    #form: HTMLFormElement
    
    constructor (inputs: Input[], button: Button) {
        this.#inputs = inputs

        this.#inputsHTML = inputs.map((input: Input) => {
            const inputElem =  document.createElement('input')
            inputElem.setAttribute('type', input.type)
            inputElem.setAttribute('name', input.name)
            if (input.placeholder) inputElem.setAttribute('placeholder', input.placeholder)
            if (input.title) inputElem.setAttribute('title', input.title)
            if (input.value) inputElem.setAttribute('value', input.value)
            
            const label = document.createElement('label')
            label.textContent = input.label
            label.appendChild(inputElem)

            return label
        })
        
        const btnElem = document.createElement('button')
        btnElem.setAttribute('type', button.type)
        btnElem.textContent = button.text
        btnElem.onclick = button.callback
        this.#button = btnElem

        const formElem = document.createElement('form')
        this.#inputsHTML.forEach((input) => {
            formElem.appendChild(input)
        })
        formElem.appendChild(btnElem)
        this.#form = formElem
    }

    validateForm () {
        const htmlInputs = this.#inputsHTML.map((label) => label.querySelector('input')!)
        
        return this.#inputs.every(({ validators, name }) => {
            const value = htmlInputs.find((input) => input.name === name)!.value
            return validators.every((validator) => validator(value))
        })
    }


}
