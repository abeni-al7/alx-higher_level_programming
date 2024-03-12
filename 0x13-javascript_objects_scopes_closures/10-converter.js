#!/usr/bin/node
exports.converter = function (base) {
  function convertToBase (num) {
    if (num < base) {
      return num < 10 ? num.toString() : String.fromCharCode(num + 87);
    } else {
      return convertToBase(Math.floor(num / base)) + (num % base < 10 ? num % base : String.fromCharCode(num % base + 87));
    }
  }

  return convertToBase;
};
