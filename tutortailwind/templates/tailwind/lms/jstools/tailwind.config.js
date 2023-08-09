module.exports = {
  important: true,
  content: [
    '../**/templates/*.html',
    '../**/templates/**/*.html'
  ],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Vazirmatn', 'Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Roboto', 'Helvetica', 'Arial', 'sans-serif'],
      },
      height: {
        '120': '30rem',
      },
      colors: {
        jescolor: {
          50:  '#E0F2C2',
          100: '#E0F2C2',
          200: '#C9E59B',
          300: '#B2D874',
          400: '#9BCB4D',
          500: '#6ca93d',
          600: '#5A8C34',
          700: '#486F2B',
          800: '#365222',
          900: '#243519',
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}