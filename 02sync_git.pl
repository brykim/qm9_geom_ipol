#!/usr/bin/perl

#################
## SUBROUTINES ##
#################

sub read_file {
      @array = (); @cntr = (); #clear temporary array and column counter
      open (IN,$_[0]) or die ("Error: file ($_[0]) not found!\n");
      $nrow = 1; #initialize row variable to zero
      while(<IN>) {
            chomp; @line = split (/\s+/,$_);
            $col = (); $col = @line; #clear column variable then  count entries on a line (starts from 0)
            push @{$array[$nrow]}, $nrow;
            foreach $column (@line) {
                  push @{$array[$nrow]}, $column; #row starts at [1] and column starts at [1] if there are no indents
                  $cntr[$nrow] =  $col;
            }
            $nrow++;
      }
      $row = $nrow-1;

      close (IN);
}

################
## MAIN BLOCK ##
################

read_file(".gitignore");
print ".gitignore the following:\n";

for $i (1 .. $row) {
$CC=<<"CC";
    $array[$i][1]
CC
printf "$CC";
}

$CC=<<'CC';

Make sure the following are completed:
    .gitignore
    README.md

Insert comment for commit (Otherwise Ctrl+C):
CC
printf "$CC";
$comment = <STDIN>;
chomp $comment;

$CC=<<"CC";
git pull
git rm -r --cached *
git add .
git status
git commit -m "$comment";
git push
CC
printf "\n$CC\n";
system "$CC";

##############
## END MAIN ##
##############

