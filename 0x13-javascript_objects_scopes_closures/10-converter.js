#!/usr/bin/node

exports.converter = function (base) {
  const converted = function (num) {
    if (num === 0) {
      return '';
    } else {
      return converted(Math.floor(num / base)) + (num % base).toString(base);
    }
  };

  return converted;
};
