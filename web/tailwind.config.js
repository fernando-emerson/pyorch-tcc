/** @type {import('tailwindcss').Config} */
import catppuccin from '@catppuccin/daisyui'

module.exports = {
  content: ["./src/**/*.{html,ts}"],
  theme: {
    extend: {
      padding: {
        '3rem': '3rem',
        '4rem': '4rem',
        '5rem': '5rem',
      }
    },
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["night", "light", "dark"],
  },
}

