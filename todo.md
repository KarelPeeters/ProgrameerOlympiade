# TODO
* update parsing utility functions to work on stdin/out
* check if we need a test runner framework or if the provided one is good enough
* check bringing monitor and keyboard
* collect more utils?:
  * pathfind
  * set cover problem
  * TSP
  * full ILP solver?
* write a proper template with utils, main function, main header, ...
  * including case count parsing and output
* fallback rust/C template for if python really is too slow?
* Floyd Marshall

# Notes

Languages:
* Python 3.9.7
  * docs are offline in ignored folder
* C/C++
  ```
  Versie            gcc version 11.2.0
  Extensie          c, cpp, cc, c++
  Compileervlaggen  gcc/g++ -Wall -O2 -static -o test test.c -lm
  Uitvoering        ./test
  Opmerkingen       main() moet eindigen met return 0;
  ```
  * TODO: collect cpp docs and figure out IO parsing?
* Rust
  ```
  Versie            1.67.0
  Extensie          rs
  Compileervlaggen  cargo build --target i686-unknown-linux-musl --release
  Uitvoering        ./a.out
  ```
  * docs are offline through cargo doc