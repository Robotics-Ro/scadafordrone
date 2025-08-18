``` mermaid
graph TD
    subgraph "1. 데이터 취득 (Data Acquisition)"
        A[🚁 Tello 드론] -- "Wi-Fi (UDP)" --> B(Tello SDK <br> 예: DJITelloPy on Python);
        B -- "상태 데이터 (Port 8890) <br> 자세, 고도, 배터리" --> C;
        B -- "영상 스트림 (Port 11111)" --> C;
    end

    subgraph "2. 동기화・처리 코어 (Synchronization & Processing Core)"
        C(실시간 데이터 <br> 매핑 로직);
        C -- "위치・자세 데이터 적용" --> D;
        C -- "영상 데이터 전송" --> E;
        C -- "각종 데이터 전송" --> F;
    end

    subgraph "3. SCADA 시각화・응용 (SCADA Visualization & Application)"
        D(<b>3D 모델 동기화</b> <br> USDZ 모델);
        E(<b>컴퓨터 비전</b> <br> YOLOv3를 이용한 객체 감지);
        F(<b>데이터 시각화</b> <br> 그래프 표시 <br> 예: Matplotlib, Plotly);
        G(<b>데이터 오버레이</b> <br> 감지 결과나 상태를 3D/AR 스타일로 표시);
        
        D & E & F & G -- "OPC UA 등의 프로토콜로 통합" --> H{SCADA HMI <br> 대시보드};
    end

    subgraph "4. 포트폴리오용 데모 제안 (Portfolio Demo Ideas)"
        P1["<b>데모 1: 기본 동기화</b><br>Tello의 움직임을 Unity의<br>3D 모델로 재현 + 그래프 표시"];
        P2["<b>데모 2: CV/AR 연동</b><br>카메라 영상에서 객체를 감지하여<br>결과를 3D 모델에 오버레이"];
        P3["<b>데모 3: ROS 연동</b><br>ROS2로 데이터를 발행하여<br>Gazebo 시뮬레이터에서 시각화"];
    end

    H -.-> P1;
    H -.-> P2;
    H -.-> P3;

    style A fill:#D6EAF8,stroke:#3498DB
    style B fill:#D5F5E3,stroke:#2ECC71
    style C fill:#FCF3CF,stroke:#F1C40F
    style H fill:#FADBD8,stroke:#E74C3C

```