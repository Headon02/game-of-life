# Conway's Game of Life

# specific how many octaves, lowest frequency, scale, synths, note length
n = 3
lf = 48
s = :minor_pentatonic
livesynth = :tri
deadsynth = :fm
d = 0.3

# plays the game
define :keysmith do |st, n|
  sc = (scale lf, s)
  l = (scale lf, s, num_octaves: n).length()
  
  return sc, l
end

keys, l = keysmith lf, n

define :init do
  field = []
  duplicate = []
  l.times do
    row = []
    l.times do
      row << rrand_i(0,1)
    end
    field << row
    duplicate << row
  end
  
  return field, duplicate
end

y0, dy = init

define :foo do |key, i, j|
  ai = (100.0 - 100*i/l)/100.0
  aj = (100.0 - 100*j/l)/100.0
  
  play (scale key, s, num_octaves: n)[i], amp: ai
  play (scale key, s, num_octaves: n)[j], amp: aj
  sleep d
end

define :count do |x, y|
  if x >= l
    x = 0
  end
  
  if y >= l
    y = 0
  end
  
  i = y0[y][x]
  
  return i
end

define :neighbor do |x, y|
  n = count x-1, y-1
  n += count x, y-1
  n += count x+1, y-1
  n += count x-1, y
  n += count x+1, y
  n += count x-1, y+1
  n += count x, y+1
  n += count x+1, y+1
  
  return n
end

define :game do
  i = 0
  l.times do
    j = 0
    l.times do
      n = neighbor j, i
      
      if n == 3
        dy[i][j] = 1
      end
      
      if n > 3
        dy[i][j] = 0
      end
      
      if n < 2
        dy[i][j] = 0
      end
      
      j += 1
    end
    
    i += 1
  end
  
  i = 0
  l.times do
    j = 0
    l.times do
      y0[i][j] = dy[i][j]
      j += 1
    end
    i+=1
  end
end

loop do
  key = keys.tick
  i = 0
  l.times do
    j = 0
    l.times do
      if y0[i][j] == 1
        use_synth livesynth
        foo key, i, j
      else
        use_synth deadsynth
        foo key, i, j
      end
      j += 1
    end
    i += 1
  end
  game
end