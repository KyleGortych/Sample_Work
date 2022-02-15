/*
 * verilog ex. hello world
 *
 * Maintainer: Kyle Gortych
 * Date:       02-09-2022
 */

module hello;
  initial 
    begin
      $display("Hello World!");
      $finish ;
    end
endmodule
