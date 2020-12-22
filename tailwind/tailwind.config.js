module.exports = {
  purge: [],
  darkMode: 'class', // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
  purge: {
    enabled: true, //true for production build
    content: [
        '../templates/*.html',
        '../templates/**/*.html'
    ],
    options: {
      safelist: ['dark', /^text-(red|blue|gray|green)-500/]
    }
  },
}
