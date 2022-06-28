-- name: get-doc-bodies
select doc_id, body from foiarchive.un_archives_docs
    where body is not null
    order by doc_id;
