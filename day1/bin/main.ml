[@@@warnerror "-unused-value-declaration"]

let input_file = "input.txt"

let my_split x = String.split_on_char ' ' x |> List.filter (fun s -> s <> "")

(* let rec make_list l = 
  match l with
  | [] -> []
  | x :: xs ->  *)

let read_lines name : string list =
  let ic = open_in name in
  let try_read () =
    try Some (input_line ic) with End_of_file -> None in
  let rec loop acc = match try_read () with
    | Some s -> loop (s :: acc)
    | None -> close_in ic; List.rev acc in
  loop []

let rec make_lists l =
  match l with
  | [] -> ([], [])
  | x :: xs -> let foo = my_split x in
    let a = List.hd foo and b = List.nth foo 1 in 
    let rest = make_lists xs in 
    ((int_of_string a)::fst rest, (int_of_string b):: snd rest)

let () = print_endline "hi there";
  let lines = read_lines input_file in
  let lists = make_lists lines in
  let al = List.sort (fun x y -> x - y) (fst lists) and 
  bl = List.sort (fun x y -> x - y) (snd lists) in
  print_endline "List 1";
  List.iter (Printf.printf "%d\n") al;
  print_endline "List 2";
  List.iter (Printf.printf "%d\n") bl;
  let diff = List.fold_left2 (fun acc a b -> acc + abs (a - b)) 0 al bl in 
  Printf.printf "Part 1 - Total diff: %d\n" diff;
  (* Part 2 *)
  let similarity = List.fold_left
    (fun acc a -> acc + a * List.length (List.filter (fun x -> x = a) bl ))
    0 al in 
  Printf.printf "Part 2 - Similarity score: %d\n" similarity;
  
