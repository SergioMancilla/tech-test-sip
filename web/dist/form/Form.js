export class Form {
    #inputs;
    #method;
    #action;
    #onSubmit;
    constructor(inputs, method, action, onSubmit) {
        this.#inputs = inputs;
        this.#method = method;
        this.#action = action;
        this.#onSubmit = onSubmit;
    }
    validateForm(newInputs) {
        return newInputs.every(({ value, validators }) => {
            validators.every((validator) => validator(value));
        });
    }
    getInputs() {
        return this.#inputs;
    }
    getMethod() {
        return this.#method;
    }
    getAction() {
        return this.#action;
    }
    getSubitAction() {
        return this.#onSubmit;
    }
}
