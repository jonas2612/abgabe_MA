#code für weights_unlabeled.csv
paste -d ';' <(cat tp0875/unbalanced.py | grep -E "\-=" | cut -f 1 -d ')' | cut -f 3 -d '-') <(cat tp0875/unbalanced.py | grep -E "\-=" | cut -f 1 -d '-' | cut -c 17-32) <(cat tp0875/unbalanced.py | grep -E "\-=" | cut -f 4 -d\')

#code für number_weights_per_tp.csv
cat tp0875/unbalanced.py | grep -E "\-=" | wc -l