// Utility Functions

/**
 * Local Storage Manager
 */
const Storage = {
    set: (key, value) => {
        localStorage.setItem(key, JSON.stringify(value));
    },
    
    get: (key) => {
        const item = localStorage.getItem(key);
        return item ? JSON.parse(item) : null;
    },
    
    remove: (key) => {
        localStorage.removeItem(key);
    },
    
    clear: () => {
        localStorage.clear();
    }
};

/**
 * Cookie Manager
 */
const Cookie = {
    set: (name, value, days = 7) => {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        const expires = `expires=${date.toUTCString()}`;
        document.cookie = `${name}=${value};${expires};path=/`;
    },
    
    get: (name) => {
        const nameEQ = `${name}=`;
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.indexOf(nameEQ) === 0) {
                return cookie.substring(nameEQ.length);
            }
        }
        return null;
    },
    
    remove: (name) => {
        Cookie.set(name, '', -1);
    }
};

/**
 * Element utilities
 */
const Dom = {
    getElementById: (id) => document.getElementById(id),
    querySelector: (selector) => document.querySelector(selector),
    querySelectorAll: (selector) => document.querySelectorAll(selector),
    
    hasClass: (element, className) => element.classList.contains(className),
    addClass: (element, className) => element.classList.add(className),
    removeClass: (element, className) => element.classList.remove(className),
    toggleClass: (element, className) => element.classList.toggle(className),
    
    show: (element) => {
        element.style.display = 'block';
    },
    
    hide: (element) => {
        element.style.display = 'none';
    },
    
    toggleVisibility: (element) => {
        element.style.display = element.style.display === 'none' ? 'block' : 'none';
    }
};

/**
 * Math utilities
 */
const Math2 = {
    roundTo: (num, decimals = 2) => {
        return Math.round(num * Math.pow(10, decimals)) / Math.pow(10, decimals);
    },
    
    percentage: (part, whole) => {
        return (part / whole) * 100;
    },
    
    random: (min, max) => {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }
};

/**
 * Array utilities
 */
const ArrayUtils = {
    shuffle: (array) => {
        let arr = [...array];
        for (let i = arr.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        return arr;
    },
    
    unique: (array) => [...new Set(array)],
    
    flatten: (array) => array.flat(Infinity),
    
    groupBy: (array, key) => {
        return array.reduce((result, item) => {
            const group = item[key];
            if (!result[group]) result[group] = [];
            result[group].push(item);
            return result;
        }, {})
    },
    
    findIndex: (array, predicate) => {
        return array.findIndex(predicate);
    }
};

/**
 * String utilities
 */
const StringUtils = {
    trim: (str) => str.trim(),
    
    toUpperCase: (str) => str.toUpperCase(),
    
    toLowerCase: (str) => str.toLowerCase(),
    
    capitalize: (str) => str.charAt(0).toUpperCase() + str.slice(1),
    
    reverse: (str) => str.split('').reverse().join(''),
    
    truncate: (str, length) => {
        return str.length > length ? str.substring(0, length) + '...' : str;
    },
    
    replaceAll: (str, search, replace) => {
        return str.split(search).join(replace);
    }
};

/**
 * Date utilities
 */
const DateUtils = {
    now: () => new Date(),
    
    format: (date, format = 'YYYY-MM-DD') => {
        const d = new Date(date);
        const year = d.getFullYear();
        const month = String(d.getMonth() + 1).padStart(2, '0');
        const day = String(d.getDate()).padStart(2, '0');
        
        return format
            .replace('YYYY', year)
            .replace('MM', month)
            .replace('DD', day);
    },
    
    addDays: (date, days) => {
        const result = new Date(date);
        result.setDate(result.getDate() + days);
        return result;
    },
    
    getMonthName: (monthIndex) => {
        const months = ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December'];
        return months[monthIndex];
    }
};

/**
 * Logger utility
 */
const Logger = {
    log: (message, data = null) => {
        console.log(`[LOG] ${message}`, data || '');
    },
    
    error: (message, data = null) => {
        console.error(`[ERROR] ${message}`, data || '');
    },
    
    warn: (message, data = null) => {
        console.warn(`[WARN] ${message}`, data || '');
    },
    
    debug: (message, data = null) => {
        console.debug(`[DEBUG] ${message}`, data || '');
    }
};

/**
 * Throttle function to limit function call frequency
 */
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    }
}

/**
 * Check if element is in viewport
 */
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}
