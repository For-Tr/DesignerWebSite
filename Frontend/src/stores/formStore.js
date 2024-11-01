// stores/formStore.js
import { defineStore } from 'pinia';

export const useFormStore = defineStore('form', {
  state: () => ({
    form: {
      text1: undefined,
      text2: undefined,
      text3: undefined,
      text4: undefined,
      text5: undefined,
      text6: undefined,
      text7: undefined,
      text8: undefined,
      text9: undefined,
      text10: undefined,
      text11: undefined,
      text12: undefined,
      text13: undefined,
      text14: undefined,
      pic1: undefined,
      pic2: undefined,
      pic3: undefined,
      pic4: undefined,
      pic5: undefined,
      pic6: undefined,
      temp: undefined,
    }
  }),
  actions: {
    updateTextField(field, value) {
      if (Object.prototype.hasOwnProperty.call(this.form, field)) {
        this.form[field] = value;
      }
    },
    updatePicField(field, value) {
      if (Object.prototype.hasOwnProperty.call(this.form, field)) {
        this.form[field] = value;
        console.log(this.form)
      }
    }
  }
});