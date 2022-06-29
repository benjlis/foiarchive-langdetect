create table doc_lang_temp (
    item_id         integer  primary key,
    doc_lang        text     not null,
    score           decimal
    );
\copy doc_lang_temp from 'whatlang.csv' delimiter ',' csv header
