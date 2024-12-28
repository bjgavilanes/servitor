let
  sources = import ./npins;
  pkgs = import sources.nixpkgs {};
in

pkgs.mkShellNoCC {
  packages = with pkgs; [
    uv
    ruff
  ];
}
