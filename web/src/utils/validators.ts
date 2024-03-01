export const validators = {
    required: (value: string) => {
        return value != null
    },
    
    isEmpty: (value: string) => {
        return value != ''
    },
    
    isNumber: (value: string) => {
        return Number.isNaN(value)
    },

    phone: (value: string) => {
        return /(\d{3})(\d{3})(\d{4})/.test(value)
    }
}