telloIP = '192.168.10.1'; % Tello 드론의 기본 IP 주소
telloPort = 8889; % Tello 드론의 명령 포트

telloUDP = udp(telloIP, 'RemotePort', telloPort, 'LocalPort', 9000);
fopen(telloUDP);

command = 'command';
fwrite(telloUDP, command);