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
    
type state = { incr: int; prev: int; safe: bool; ix: int }
let is_safe ?(ignore_ix = -1) (rs : int list)  = 
  let safe_state = 
    let rs = if ignore_ix = 0 then List.tl rs else rs in
    let first_item = List.hd rs in 
    let first_index = if ignore_ix = 0 then 2 else 1 in
     
    List.fold_left (fun s x -> match s with
    | { incr; prev; safe=false; ix} -> {incr; prev; safe=false; ix=ix+1}
    | { incr; prev; safe; ix} when ix = ignore_ix -> {incr; prev; safe; ix=ix+1}
    | { incr = 0; prev; safe; ix } when x > prev && x <= prev + 3 -> {incr = 1; safe; prev = x; ix = ix+1 }
    | { incr = 0; prev; safe; ix } when x < prev && x >= prev - 3 -> {incr = -1; safe; prev = x; ix = ix+1 }
    | { incr = 1; prev; safe; ix } when x - prev <= 3 && x > prev -> {incr = 1; safe; prev = x; ix=ix+1 }
    | { incr = -1; prev; safe; ix } when prev - x <= 3 && x < prev -> {incr = -1; safe; prev = x;ix=ix+1 }
    | {incr; prev; safe=_; ix} -> { safe = false; incr; prev; ix=ix+1} )
    { incr = 0; prev = first_item ; safe = true; ix = first_index } (List.tl rs) in 
    (* Printf.printf "State: {i: %d; p: %d; s: %s} ignoring %d\n" safe_state.incr safe_state.prev (string_of_bool safe_state.safe) ignore_ix; *)
  safe_state.safe

let is_safe_with_damper rs =
  (* iterate over indexes in rs, skip selected index, safe if any is safe *)
    List.exists (fun x->x) (List.mapi (fun i _ -> is_safe ~ignore_ix:i rs) rs)

let () = 
  let lines = read_lines input_file in
  (* let reports = List.map (String.split_on_char ' ') lines in  *)
  let reports = List.map (fun s -> List.map int_of_string (String.split_on_char ' ' s )) lines in 
  Printf.printf "Reports (len: %d)\n" (List.length reports);
  let print_report r =  
    List.iter (Printf.printf "%d ") r; 
    Printf.printf " - %s\n" (if is_safe r then "Safe" else "NOT SAFE"); in
  List.iter (print_report) reports;
  let number_of_safe = List.length (List.filter is_safe reports) in
  Printf.printf "\nPart 1: Total number of safe reports: %d\n" number_of_safe;
  
  let number_of_safe_with_dampener = List.length (List.filter is_safe_with_damper reports) in
  List.iter (fun r -> List.iter (Printf.printf "%d ") r; Printf.printf " - %s\n" (if is_safe_with_damper r then "Safe" else "NOT SAFE");) reports;
  Printf.printf "\nPart 2: Total number of safe reports: %d\n" number_of_safe_with_dampener 