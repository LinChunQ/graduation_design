import { createI18n } from 'vue-i18n';
// 项目语言包文件
import localEn from './language/en';
import localZhCn from './language/zh-cn';

// element-plus 语言包文件
import en from 'element-plus/es/locale/lang/en';
import zhCn from 'element-plus/es/locale/lang/zh-cn';

// project i18n
const i18n = createI18n({
    legacy: false,  // vue组合式api设为false
    locale: 'zh-cn',  // 默认语言
    fallbackLocale: 'en', // 回退语言
    messages: {
        'zh-cn': localZhCn,
        'en': localEn
    }
});

// element i18n
export const elementLocales = {
    'zh-cn': zhCn,
    en
};

export default i18n;
