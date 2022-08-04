# Refactored brew List Packages No Dependancies

## fish Shell Aliases
Defined in ~/.config/fish/config.fish

``` fish
function brew-pkgs-nodepens
  column -t -s '|' ~/.config/CLI\ Support/aliase\ \&\ script\ support/brew-pkgs.txt | tr '*' ' '
end

function brew-active-pkgs-nodepens
  echo -e '\e[4mPackages no Depens\e[0m' ; brew leaves | column ; echo '' ; echo -e '\e[4mCasks\e[0m' ; brew list --cask
end
```

## Future Automated Refactoring
Auto: Being worked on…

Manualy: Past & edit text file in vim ie copy from brew leaves past in vim then substitute args for parames for num and delimiter_type
``` vim
:num1,num2 s/\s\+/delimiter_type/g
```

## Approximately a 300x Speedup

<img width="1000" alt="refactored aliase" src="https://user-images.githubusercontent.com/99693659/182916579-d014592f-f439-4945-816d-998d31f4b5ec.png">
