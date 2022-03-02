Require Import Unicode.Utf8.

Inductive boolean : Type := 
  | true : boolean
  | false : boolean.

Definition or ( x y : boolean) : boolean := 
  match x with
  | true => true
  | false => y
  end.

Theorem boolean_or_false : ∀ a : boolean, or a false = a.
