export const validators = {
    required: (value) => {
        return {
            val: !!value,
            msg: 'The field is required'
        };
    },
    isEmpty: (value) => {
        return {
            val: value != '',
            msg: 'The value cannot be empty'
        };
    },
    isNumber: (value) => {
        return {
            val: !Number.isNaN(value),
            msg: 'The field must be a number'
        };
    },
    phone: (value) => {
        return {
            val: /^\+?\d{0,3}\d{10}$/.test(value),
            msg: 'Enter a valid phone'
        };
    },
    isDate: (value) => {
        const dateObject = new Date(value);
        return {
            val: !isNaN(dateObject.getTime()) && dateObject.toISOString().slice(0, 10) === value,
            msg: 'Enter a valid date'
        };
    },
    beforeToday: (value) => {
        const msg = 'Enter a date before today';
        if (!validators.isDate(value)['val']) {
            return { val: false, msg };
        }
        const today = new Date();
        const dateValue = new Date(value);
        today.setHours(0, 0, 0, 0);
        dateValue.setHours(0, 0, 0, 0);
        return {
            val: dateValue < today,
            msg
        };
    }
};
