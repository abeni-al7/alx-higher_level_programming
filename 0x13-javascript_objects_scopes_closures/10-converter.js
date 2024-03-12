#!/usr/bin/node
exports.converter = function (base) {
  function convertToBase (num) {
    if (num < base) {
      return num.toString();
    } else {
      return convertToBase(Math.floor(num / base)) + (num % base).toString();
    }
  }

  return convertToBase;
};
