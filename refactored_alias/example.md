# Refactored brew list packages no dependancies

## fish shell aliases
Defined in ~/.config/fish/config.fish

``` fish
function brew-pkgs-nodepens
  column -t -s '|' ~/.config/CLI\ Support/aliase\ \&\ script\ support/brew-pkgs.txt | tr '*' ' '
end

function brew-active-pkgs-nodepens
  echo -e '\e[4mPackages no Depens\e[0m' ; brew leaves | column ; echo '' ; echo -e '\e[4mCasks\e[0m' ; brew list --cask
end
```

## Approximately a 300x Speedup

<img width="1000" alt="refactored aliase" src="https://user-images.githubusercontent.com/99693659/182916579-d014592f-f439-4945-816d-998d31f4b5ec.png">
