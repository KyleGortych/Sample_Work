# Refactored brew List Packages No Dependancies

## A Modest Speedup

<img width="1000" alt="refactored aliase" src="https://raw.githubusercontent.com/KyleGortych/sample_work/main/refactored_alias/Refactored%20brew%20list.png">

## fish Shell Aliases

<details>
<summary>example</summary>

``` fish
function brew-ls
  cat ~/path/file
end

function brew-seach
  echo -e '\e[4mPackages no Depens\e[0m' ; brew leaves | column ; echo '' ; echo -e '\e[4mCasks\e[0m' ; brew list --cask ; echo '' ; echo -e '\e[4mTaps\e[0m' ; brew tap-info --installed
end
```
</details>

## Semi-Auto
<details>
<summary>Past from brew-search ie. example alias, then visual select to edit text file. Lastly use command below while in visual mode.</summary>
  
``` vim
:'<,'>!column -t
```

</details>

## result
<details>
<summary>example</summary>
<pre>
  Packages no Depens
  -------------------
  pkg1 pkg4 pkg7
  pkg2 pkg5 pkg8
  pkg3 pkg6 pkg9
</pre>
<pre>
  Casks
  ------
  cask1 cask4 cask7
  cask2 cask5 cask8
  cask3 cask6 cask9
</pre>
<pre>
  Taps/3d Party
  --------------
  name: num casks
  /usr/local/Homebrew/Library/Taps/ (num files, num KB)
  From: https://github.com/pkg-name
</pre>
</details>
