put-child (new: NODE) is
  -- Add new to the children of current node
  require
    new/= Void
  do
    ... Insertion algorithm ...
  ensure
      new.parent = Current;
      child-count = old child-count + 1
  end
