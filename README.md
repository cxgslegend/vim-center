## Installation
Plug 'cxgslegend/vim-center'

## Usage
If your cursor is on the following line 
> ** some text|||

If you then type  
> :CenterText 

It will result in the "some text" part of the string being centered within a 80 column width, with delimiters.  
> ***                                some text                                 ***

## Remapping
`nnoremap <leader>ct :CenterText<cr>`

If you want a width other than 80, just use CenterTextOfLength command instead. 


`nnoremap <leader>ct :CenterTextOfLength 70<cr>`

## Rules used for centering text within delimiters

The general rules for centering some text within delimiters are 
1) We make sure the delimiters are the same on the left and right, and they are approximatly the same length (they should always be within 1 character of each other). 
2) If we can center the text within the given length, we simply center the text (the default length is 80). 
3) If we cannot center the text within the given length, see if we can fit it if we truncate the text. 
4) If even after truncating the text, we cannot fit the text, try truncating the delimiters. 
5) If we still cannot fit within the given length, try truncating the space between the delimiters and the center text.
6) If we still cannot fit within the given length, drop all delimiters, and spaces, and simply print as many characters as you can. 

For the following line, these are how it would look like for different widths. 

**something example text|||

```
                                                    (0)
s                                                   (1)
so                                                  (2)
*s*                                                 (3)
* s*                                                (4)
* s *                                               (5)
** s *                                              (6)
** s **                                             (7)
*** s **                                            (8)
*** s ***                                           (9)
*** so ***                                          (10)
*** som ***                                         (11)
*** some ***                                        (12)
*** somet ***                                       (13)
*** someth ***                                      (14)
*** somethi ***                                     (15)
*** somethin ***                                    (16)
*** something ***                                   (17)
*** something  ***                                  (18)
*** something e ***                                 (19)
*** something ex ***                                (20)
*** something exa ***                               (21)
*** something exam ***                              (22)
*** something examp ***                             (23)
*** something exampl ***                            (24)
*** something example ***                           (25)
*** something example  ***                          (26)
*** something example t ***                         (27)
*** something example te ***                        (28)
*** something example tex ***                       (29)
*** something example text ***                      (30)
***  something example text ***                     (31)
***  something example text  ***                    (32)
***   something example text  ***                   (33)
***   something example text   ***                  (34)
***    something example text   ***                 (35)
***    something example text    ***                (36)
***     something example text    ***               (37)
***     something example text     ***              (38)
***      something example text     ***             (39)
***      something example text      ***            (40)
***       something example text      ***           (41)
***       something example text       ***          (42)
***        something example text       ***         (43)
***        something example text        ***        (44)
***         something example text        ***       (45)
***         something example text         ***      (46)
***          something example text         ***     (47)
***          something example text          ***    (48)
                     .
                     .
                     .
```
