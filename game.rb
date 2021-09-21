# Conway's Game of Life

# specific how many octaves, lowest frequency, scale, synths, volume, note length
num = 1
lf = 60
s = :minor_pentatonic
livesynth = :tri
deadsynth = :fm
livevol = 1
deadvol = 0.5
d = 0.3

# patterns
patterns = {
  
  0 => [[1, 1],
        
        [1, 1]], # block
  
  1 => [[0, 1, 1, 0],
        
        [1, 0, 0, 1],
        
        [0, 1, 1, 0]], #beehive
  
  2 => [[0, 1, 1, 0],
        
        [1, 0, 0, 1],
        
        [0, 1, 0, 1],
        
        [0, 0, 1, 0]], # loaf
  
  3 => [[1, 1, 0],
        
        [1, 0, 1],
        
        [0, 1, 0]], # boat
  
  4 => [[0, 1, 0],
        
        [1, 0, 1],
        
        [0, 1, 0]], # tub
  
  5 => [[1],
        
        [1],
        
        [1]], # blinker
  
  6 => [[0, 1, 1, 1],
        
        [1, 1, 1, 0]], # toad
  
  7 => [[1, 1, 0, 0],
        
        [1, 1, 0, 0],
        
        [0, 0, 1, 1],
        
        [0, 0, 1, 1]], # beacon
  
  8 => [[0, 1, 0],
        
        [0, 0, 1],
        
        [1, 1, 1]], # glider
  
  9 => [[0, 1, 1],
        
        [1, 1, 0],
        
        [0, 1, 0]], # r-pentomino
  
  10 => [[0, 0, 0, 0, 0, 0, 1, 0],
         
         [1, 1, 0, 0, 0, 0, 0, 0],
         
         [0, 1, 0, 0, 0, 1, 1, 1]], # diehard
  
  11 => [[0, 1, 0, 0, 0, 0, 0],
         
         [0, 0, 0, 1, 0, 0, 0],
         
         [1, 1, 0, 0, 1, 1, 1]], # acorn
  
  12 => [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] # gosper glider gun
}

# plays the game
define :keysmith do |st, n|
  sc = (scale lf, s)
  sl = (scale lf, s, num_octaves: n)
  k = []
  i = 0
  (sc.length() - 1).times do
    k << sc[i]
    i += 1
  end
  
  m = []
  i = 0
  (sl.length() - 1).times do
    m << sl[i]
    i += 1
  end
  
  l = m.length()
  
  return k.ring, l, m.ring
end

keys, l, scales = keysmith lf, num

define :init do
  field = []
  duplicate = []
  l.times do
    row = []
    drow = []
    l.times do
      row << 0 #rrand_i(0,1)
      drow << 0
    end
    field << row
    duplicate << drow
  end
  
  return field, duplicate
end

y0, dy = init

define :place do |p|
  i = 0
  p.length().times do
    j = 0
    p[0].length().times do
      y0[i][j] = p[i][j]
      dy[i][j] = p[i][j]
      j += 1
    end
    i+=1
  end
end

place patterns[8]

define :foo do |key, i, j, life|
  ai = ((100.0 - 100*i/l)/100.0) * life
  aj = ((100.0 - 100*j/l)/100.0) * life
  
  play scales[i] + (key - lf), amp: ai
  play scales[j] + (key - lf), amp: aj
  sleep d
end

define :count do |x, y|
  if x == l
    x = 0
  end
  
  if y == l
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
        foo key, i, j, livevol
      else
        use_synth deadsynth
        foo key, i, j, deadvol
      end
      j += 1
    end
    i += 1
  end
  game
end