#!/usr/bin/env node

const size = parseInt(process.argv[2]);
if (size) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
