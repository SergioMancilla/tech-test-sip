export const validators = {
    required: (value) => {
        return value != null;
    },
    isEmpty: (value) => {
        return value != '';
    },
    isNumber: (value) => {
        return Number.isNaN(value);
    },
    phone: (value) => {
        return /(\d{3})(\d{3})(\d{4})/.test(value);
    }
};
