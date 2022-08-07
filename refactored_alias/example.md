# Refactored brew List Packages No Dependancies

## Approximately a 300x Speedup

<img width="1000" alt="refactored aliase" src="https://user-images.githubusercontent.com/99693659/182916579-d014592f-f439-4945-816d-998d31f4b5ec.png">

## fish Shell Aliases
Still working on removing redundancies

<details>
<summary>example</summary>

``` fish
function brew-ls
  sed -n "/Packages no Depens/,/*/p" ~/path/brew-pkgs.txt | column -t -s '|' | tr '*' ' '; sed -n "/Casks/,/*/p" ~/path/brew-pkgs.txt | column -t -s '|' | tr '*' ' '; sed -n "/Taps/,\$p" ~/path/brew-pkgs.txt | tr '*' ' '
end

function brew-seach
  echo -e '\e[4mPackages no Depens\e[0m' ; brew leaves | column ; echo '' ; echo -e '\e[4mCasks\e[0m' ; brew list --cask ; echo '' ; echo -e '\e[4mTaps\e[0m' ; brew tap-info --installed
end
```
</details>
  
## Future Automated Refactoring
Auto: Being worked on…

## Manualy
<details>
<summary>Past & edit text file in vim ie copy from brew leaves past in vim then substitute args for parames for num and delimiter_type</summary>
  
``` vim
:num1,num2 s/\s\+/delimiter_type/g
```

</details>
