export interface Input {
    id: string,
    type: string
    name: string
    label: string
    placeholder?: string
    title?: string
    value?: string
    validators: Validator[]
}

type Validator = (value: string) => boolean
export type SubmitAction = (...args: any[]) => void
export type Method = 'GET' | 'POST'

export class Form {
    #title?: string
    #inputs: Input[]
    #method: Method
    #action: string
    #onSubmit: SubmitAction
    
    constructor (inputs: Input[], method: Method, action: string, onSubmit: SubmitAction, title: string = '') {
        this.#inputs = inputs
        this.#method = method
        this.#action = action
        this.#onSubmit = onSubmit
        this.#title = title
    }

    getInputs (): Input[] {
        return this.#inputs
    }

    getMethod (): Method {
        return this.#method
    }

    getAction (): string {
        return this.#action
    }

    getTitle (): string | undefined {
        return this.#title || undefined
    }

    runSubmitAction (...args: any[]): void {
        return this.#onSubmit(args)
    }
}
