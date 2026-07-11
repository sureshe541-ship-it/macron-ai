{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.nodejs_24
    pkgs.postgresql_16
    pkgs.pnpm
  ];
}
