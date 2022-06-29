-- name: get-ids
select doc_id from foiarchive.un_archives_docs
    where body is not null
    order by doc_id;

-- name: get-body
-- The spaCy parser and NER models require roughly 1GB of temporary memory per
-- 100,000 characters in the input. This means long texts may cause memory
-- allocation errors. If you're not using the parser or NER, it's probably safe
-- to increase the `nlp.max_length` limit. The limit is in number of characters,
-- so you can check whether your inputs are too long by checking `len(text)`.
select substr(body, 1, 800000) from foiarchive.un_archives_docs
    where doc_id = :doc_id;

-- name: get-doc-bodies
select doc_id, body from foiarchive.un_archives_docs
    where body is not null
    order by doc_id;
