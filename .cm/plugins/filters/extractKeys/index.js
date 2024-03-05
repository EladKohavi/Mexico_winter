module.exports = (text) => {
  return text.match(/password=([^\s]+)/g);
}
