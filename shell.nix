{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs.python3Packages; [
    python
    pypdf2
    tabula-py
    # Add any additional Python packages you need here
  ];
}
