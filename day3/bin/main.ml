[@@@warnerror "-unused-value-declaration"]

let filename = "input.txt"

let read_whole_file filename =
  (* open_in_bin works correctly on Unix and Windows *)
  let ch = open_in_bin filename in
  let s = really_input_string ch (in_channel_length ch) in
  close_in ch;
  s
let re_mul = Re.compile Re.( 
  seq [
    str "mul(";
    group (repn digit 1 (Some 3));
    str ",";
    group (repn digit 1 (Some 3));
    str ")"
    ])

let re_token = Re.compile Re.(alt [ 
    seq [
      str "mul(";
      group (repn digit 1 (Some 3));
      str ",";
      group (repn digit 1 (Some 3));
      str ")"
      ]; 
    str "do()";
    str "don't()"])
  
let multiply m = 
  let a = int_of_string (Re.Group.get m 1) and
      b = int_of_string (Re.Group.get m 2) in 
  a * b

let process_token (state,sum) m = 
  let matching = Re.Group.get m 0 in
  match matching with 
  | "do()" -> true, sum
  | "don't()" -> false, sum
  | _ when state -> state, sum + multiply m
  | _ -> state, sum

let () = print_endline "Hello, World!";
  (* let input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))" in  *)
  let input = read_whole_file filename in
  let matches = Re.all re_mul input in
  List.iter (fun m -> Printf.printf "%s x %s\n" (Re.Group.get m 1) (Re.Group.get m 2)) matches;
  let sum = List.fold_left (fun s m -> s + multiply m) 0 matches in
  Printf.printf "Part1: Sum= %d\n" sum;

  let matches = Re.all re_token input in
  List.iter (fun m -> 
    let m0 = Re.Group.get m 0 in 
    match m0 with | "don't()" -> print_endline "Disable" | "do()" -> print_endline "Enable" | _ -> Printf.printf "%s x %s\n" (Re.Group.get m 1) (Re.Group.get m 2)) matches;
  let _,sum2 = List.fold_left process_token (true,0) matches in
  Printf.printf "Part2: Sum= %d\n" sum2;

