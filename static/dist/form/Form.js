export class Form {
    #title;
    #inputs;
    #method;
    #action;
    #onSubmit;
    constructor(inputs, method, action, onSubmit, title = '') {
        this.#inputs = inputs;
        this.#method = method;
        this.#action = action;
        this.#onSubmit = onSubmit;
        this.#title = title;
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
    getTitle() {
        return this.#title || undefined;
    }
    runSubmitAction() {
        // A submit function will require the Form instance
        return this.#onSubmit(this);
    }
}
