# Direct substitution mappings

static_substitutions = [

    ('https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css','dpd_static_support/css'),
    ('https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js','dpd_static_support/js'),
    ("https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd", 'dpd_static_support/js'),
    ("https://code.jquery.com/jquery-3.3.1.min.js", "dpd_static_support/js/jquery-3.3.1.min.js"),

    ('https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css','dpd_static_support/css'),
    ('https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js','dpd_static_support/js'),
    ("https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd", 'dpd_static_support/js'),
]

substitutions = [

    ('integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB"', ''),  # bootstap 4.1.1 https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css
    ('integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T"', ''),  # bootstap 4.1.1 https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js
    ('integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"', ''),  # bootstrap4.1.3 https://cdn.jsdelivr.net/npm/popper.js@1.14.3/dist/umd/popper.min.js
    ('integrity="sha384-tsQFqpEReu7ZLhBV2VZlAu7zcOV+rXbYlF2cqB8txI/8aZajjp4Bqd+V6D5IgvKT"', ''),  # https://code.jquery.com/jquery-3.3.1.min.js

    ('integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"', ''),  # bootstrap 4.3 https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css
    ('integrity="sha384-tsQFqpEReu7ZLhBV2VZlAu7zcOV+rXbYlF2cqB8txI/8aZajjp4Bqd+V6D5IgvKT"', ''),  # https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js
    ('integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"', ''),  # bootstrap 4.3 https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js
    ('integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"', ''),  # bootstrap 4.3 https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js

]
