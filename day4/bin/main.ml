[@@@warnerror "-unused-value-declaration"]

let input_file = "input.txt"

let read_lines name : string list =
  let ic = open_in name in
  let try_read () =
    try Some (input_line ic) with End_of_file -> None in
    let rec loop acc = match try_read () with
    | Some s -> loop (s :: acc)
    | None -> close_in ic; List.rev acc in
    loop []

let word_square () = 
  let lines = read_lines input_file in
  Array.of_list lines

(** Find the number of times the string XMAS appears starting from x y, increasing by dx dy, ending on edge of array *)
let find_xmas square ~dx ~dy ~x ~y = 
  let xmas = ['X'; 'M'; 'A'; 'S'] in 
  let rec find_once (x,y,s) =
    (* Printf.printf "(%d, %d, %s)\n" x y (String.init (List.length s) (fun i -> List.nth s i) ); *)
    match (x,y, s) with 
      |(x, y, []) -> 1 + find_once (x+dx, y+dy, xmas)
    | (x, y, _ ) when y < 0 || y >= Array.length square || x < 0 || x >= String.length square.(y) -> 0
    | (x, y, s::ss) when s = square.(y).[x] -> find_once (x+dx, y+dy, ss)
    | (x, y, xm) when xmas=xm -> find_once (x+dx, y+dy, xmas)
    | (x, y, _) -> find_once (x, y, xmas)
   in
  let res = find_once (x, y, xmas) in 
  Printf.printf "find_xmas dx:%d dy:%d x:%d y:%d = %d\n" dx dy x y res;
  res 

let () =
let square = word_square () in 
let y1 = Array.length square - 1 in 
let x1 = String.length square.(0) - 1 in 
(* From top *)
let sum1 =  
  (Seq.fold_lefti (fun a i _-> 
    a + find_xmas square ~dx:0 ~dy:1 ~x:i ~y:0
      + find_xmas square ~dx:1 ~dy:1 ~x:i ~y:0
      + find_xmas square ~dx:(-1) ~dy:1 ~x:i ~y:0) 0 (String.to_seq square.(0))) and
  (* From bottom *)
  sum2 = (Seq.fold_lefti (fun a i _-> 
    a + find_xmas square ~dx:0 ~dy:(-1) ~x:i ~y:y1
      + find_xmas square ~dx:1 ~dy:(-1) ~x:i ~y:y1
      + find_xmas square ~dx:(-1) ~dy:(-1) ~x:i ~y:y1) 0 (String.to_seq square.(0))) and
  (* From left *)
  sum3 = (Seq.fold_lefti (fun a i _-> 
    a + find_xmas square ~dx:1 ~dy:(-1) ~x:0 ~y:(i+1)
      + find_xmas square ~dx:1 ~dy:0 ~x:0 ~y:(i+1)
      + find_xmas square ~dx:1 ~dy:1 ~x:0 ~y:(i+1)) 0 (Seq.drop 2 (Array.to_seq square))) + 
    find_xmas square ~dx:1 ~dy:0 ~x:0 ~y:0 + 
    find_xmas square ~dx:1 ~dy:0 ~x:0 ~y:y1 and 
  (* From right *)
  sum4 = (Seq.fold_lefti (fun a i _-> 
    a + find_xmas square ~dx:(-1) ~dy:(-1) ~x:x1 ~y:(i+1)
      + find_xmas square ~dx:(-1) ~dy:0 ~x:x1 ~y:(i+1)
      + find_xmas square ~dx:(-1) ~dy:1 ~x:x1 ~y:(i+1)) 0 (Seq.drop 2 (Array.to_seq square))) +
      find_xmas square ~dx:(-1) ~dy:0 ~x:x1 ~y:0 + 
      find_xmas square ~dx:(-1) ~dy:0 ~x:x1 ~y:y1 
   in
      let sum = sum1 + sum2 + sum3 + sum4 in 
Printf.printf "Total sum of XMASes = %d + %d + %d + %d = %d\n" sum1 sum2 sum3 sum4 sum;
